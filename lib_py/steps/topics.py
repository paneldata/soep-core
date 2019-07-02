from ddi.onrails.repos import copy
from ddi.onrails.repos.topics import TopicParser


def main():
    print("[INFO] Test topics converter.")
    copy.f("topics.csv")
    TopicParser(
        topics_input_csv="ddionrails/topics.csv",
        concepts_input_csv="ddionrails/concepts.csv",
    ).to_json()


if __name__ == "__main__":
    main()
