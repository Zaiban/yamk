import os
import time
import tensorflow as tf
import turicreate as tc

print(tf.test.is_gpu_available())
tc.config.set_num_gpus(1)


data = tc.SFrame.read_csv('data/clean_ratings.csv')
train, test = tc.recommender.util.random_split_by_user(data, 'userId', 'title')

print("==============")
print("START TRAINING")
print("==============")
start_time = time.time()
if os.path.isfile('movie_recs.model'):
    model = tc.loa_model('movie_recs.model')
else:
    model = tc.recommender.create(train, 'userId', 'title', target='rating')
print("==============")
print("END TRAINING", (time.time() - start_time))
print("==============")

model.save('movie_recs.model')

recommendations = model.recommend(users=[1, 30, 138491])
recommendations.print_rows(num_rows=30, num_columns=4)

