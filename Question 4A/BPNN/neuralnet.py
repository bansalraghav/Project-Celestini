import tensorflow as tf
import numpy as np




n_nodes_hl1 = 500
n_nodes_hl2 = 500
n_nodes_hl3 = 500

n_classes = 2
batch_size = 10

x = tf.placeholder('float', [None, 26])
y = tf.placeholder('float')

X=np.load("X_neuralnetwork.npy")
X_test=np.load("X_test_nn.npy")

train=X
test=X_test

train_x=np.array([i[0] for i in train])
train_y=[i[1] for i in train]

test_x=np.array([i[0] for i in test])
test_y=[i[1] for i in test]

train_x= np.array(train_x)
#x=preprocessing.scale(x)
train_y=np.array(train_y)
print(train_x.shape)
print(train_y.shape)
#y = np.ravel(y)

test_x= np.array(test_x)
#test_x=preprocessing.scale(test_x)
test_y=np.array(test_y)
print(test_x.shape)
print(test_y.shape)
#test_y = np.ravel(test_y)


def neural_network_model(data,name="nn"):
    with tf.name_scope(name):

        w=tf.Variable(tf.random_normal([26,n_nodes_hl1]), name="w1")
        
        b=tf.Variable(tf.random_normal([n_nodes_hl1]), name="b1")
                    
        
        
        hidden_1_layer = {'weights':w,'biases':b}

        hidden_2_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2]),name="w2"),
                          'biases':tf.Variable(tf.random_normal([n_nodes_hl2]),name="b2")}

        hidden_3_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3]),name="w3"),
                          'biases':tf.Variable(tf.random_normal([n_nodes_hl3]),name="b3")}

        output_layer = {'weights':tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                        'biases':tf.Variable(tf.random_normal([n_classes])),}
        
        
        tf.summary.histogram("biases",b)

        l1 = tf.add(tf.matmul(data,hidden_1_layer['weights']), hidden_1_layer['biases'])
        l1 = tf.nn.relu(l1)
        tf.summary.histogram("weights",w) 

        l2 = tf.add(tf.matmul(l1,hidden_2_layer['weights']), hidden_2_layer['biases'])
        l2 = tf.nn.relu(l2)

        l3 = tf.add(tf.matmul(l2,hidden_3_layer['weights']), hidden_3_layer['biases'])
        l3 = tf.nn.relu(l3)

        output = tf.matmul(l3,output_layer['weights']) + output_layer['biases']

        return output


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels = y,logits =prediction) )
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
    hm_epochs=50

    with tf.Session() as sess:
	    sess.run(tf.initialize_all_variables())
	    merged_summary=tf.summary.merge_all()
	    writer = tf.summary.FileWriter("tmp/nn/4")
	    writer.add_graph(sess.graph)
	    
	    for epoch in range(hm_epochs):
		    epoch_loss = 0
		    i=0
		    while i < len(train_x):
			    start = i
			    end = i+batch_size
			    batch_x = np.array(train_x[start:end])
			    batch_y = np.array(train_y[start:end])
			    if epoch%3==0:
                                s=sess.run(merged_summary,feed_dict={x:batch_x,y:batch_y})
                                writer.add_summary(s,i)

			    _, c = sess.run([optimizer, cost], feed_dict={x: batch_x,
				                                              y: batch_y})
			    epoch_loss += c
			    i+=batch_size
				
		    print('Epoch', epoch+1, 'completed out of',hm_epochs,'loss:',epoch_loss)
	    correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
	    accuracy = tf.reduce_mean(tf.cast(correct, 'float'))

	    print('Accuracy:',accuracy.eval({x:test_x, y:test_y}))
		
		

	    
train_neural_network(x)
