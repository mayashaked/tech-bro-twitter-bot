import markovify

MY_CORPUS_PATH = "mycorpus.txt"

def do_it(num_tweets = 50):
    with open(MY_CORPUS_PATH) as f:
        text = f.read()

    text_model = markovify.Text(text)


    my_tweets = []

    for i in range(num_tweets):
        tweet = text_model.make_short_sentence(140)
        print(tweet)
        my_tweets.append(tweet)

    return(my_tweets)
