import os
import time
import tensorflow as tf
import turicreate as tc

MODELFILE = 'models/movie_recs.model'
RECOMMEND_USERS = [1, 30, 13849200]

os.system("echo 'test' >> models/testfile")

print(tf.test.is_gpu_available())
tc.config.set_num_gpus(1)


data = tc.SFrame.read_csv('data/clean_ratings.csv')
train, test = tc.recommender.util.random_split_by_user(data, 'userId', 'title')

print("==============")
print("START TRAINING")
print("==============")
start_time = time.time()
if os.path.exists(MODELFILE):
    print("Using old model ...")
    model = tc.load_model(MODELFILE)
else:
    print("Creating new model ...")
    model = tc.recommender.create(train, 'userId', 'title', target='rating')
print("==============")
print("END TRAINING", (time.time() - start_time))
print("==============")

model.save(MODELFILE)

recommendations = model.recommend(users=RECOMMEND_USERS)
recommendations.print_rows(num_rows=30, num_columns=4)

os.system("echo 'complete' >> models/testfile")
