import argparse
import os

import tensorflow as tf

from six import text_type
from six.moves import cPickle

from model import Model


def main():
    tf.reset_default_graph() 
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    archivo = open("sentencia.txt", "r") 
    contenido = archivo.readlines()
    archivo.close()
    parser.add_argument('--save_dir', type=str, default='checkpoints',
                        help='model directory to store checkpointed models')
    parser.add_argument('-n', type=int, default=380,
                        help='number of characters to sample')
    #parser.add_argument('--prime', type=text_type, default=u'A row of motorcycles parked next to each other. ',
    parser.add_argument('--prime', type=text_type, default=contenido[0],
                        help='prime text')
    parser.add_argument('--sample', type=int, default=1,
                        help='0 to use max at each timestep, 1 to sample at '
                             'each timestep, 2 to sample on spaces')

    sample(parser.parse_args())


def sample(args):
    with open(os.path.join(args.save_dir, 'data\conan\config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)

    with open(os.path.join(args.save_dir, 'data\conan\chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)

    model = Model(saved_args, training=False)
    #print("Hola")
    with tf.Session() as sess:
        #print("Hola2")
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        #ckpt = tf.train.get_checkpoint_state(args.save_dir)
        ckpt = tf.train.get_checkpoint_state('checkpoints\data\conan\data')
        #print(ckpt)
        #print(ckpt.model_checkpoint_path)
        if ckpt and ckpt.model_checkpoint_path:
            #print("Hola3")
            saver.restore(sess, ckpt.model_checkpoint_path)
            samp = model.sample(sess, chars, vocab, args.n, args.prime, args.sample)
            #print(samp.encode('utf-8'))
            #print("Ejemplo: "+str(samp.encode('utf-8')))
            print("Ejemplo: "+str(samp))       	
            archivo = open("broma.txt","w")
            archivo.write(samp)
            archivo.close()

if __name__ == '__main__':
    main()
