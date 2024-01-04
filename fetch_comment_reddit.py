import praw
import pandas as pd


reddit_client_id = ''
reddit_client_secret = 'ILTEv29gdNSyGk8dOX'
reddit_user_agent = 'wonders_of'

def authenticate_reddit():
    reddit = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent=reddit_user_agent,
    )
    return reddit

def fetch_reddit_comments(subreddit, start_date, end_date, num_comments, reddit):
    comments = []
    for submission in reddit.subreddit(subreddit).new(limit=num_comments):
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            comments.append({"body": comment.body})
            if len(comments) >= num_comments:
                break
        if len(comments) >= num_comments:
            break
    return comments

def save_to_csv(comments, filename='comments.csv'):
    df = pd.DataFrame(comments)
    df.to_csv(filename, index=False)

def main():
    subreddit = "worldpolitics2"
    start_date = "2023-11-22"
    end_date = "2023-12-22"
    num_comments = 100

    reddit = authenticate_reddit()

    comments = fetch_reddit_comments(subreddit, start_date, end_date, num_comments, reddit)

    print(f"Number of comments retrieved: {len(comments)}")

    save_to_csv(comments)

if __name__ == "__main__":
    main()
