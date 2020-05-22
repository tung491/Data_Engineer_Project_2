import csv
import glob
import os
from sql_queries import *
from cassandra.cluster import Cluster


def process_song_library_session(session, filepath):
    with open(filepath, encoding='utf-8') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)
        for line in csv_reader:
            session.execute(song_library_session_insert,
                            (int(line[8]), int(line[3]),
                             line[0], line[-2], float(line[5])))


def process_song_playlist_session(session, filepath):
    with open(filepath, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            session.execute(song_playlist_session_insert,
                            (int(line[-1]), int(line[-3]), int(line[3]), line[0], line[-2], line[1], line[4]))


def process_user_song_history(session, filepath):
    with open(filepath, encoding='utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader)  # skip header
        for line in csvreader:
            session.execute(user_song_history_insert, (line[-2], int(line[-1]), line[1], line[4]))


def process_data(summary_filepath):
    """
    Read files in event_data and add it to summary file
    summary_filepath: the path file which is writed as summary file
    :return: None
    """
    filepath = os.getcwd() + '/event_data'
    for root, dirs, files in os.walk(filepath):
        file_path_list = glob.glob(os.path.join(root, '*'))
    full_data_rows_list = []
    for i, f in enumerate(file_path_list, 1):
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvfile)

            for line in csvreader:
                full_data_rows_list.append(line)
        num_files = len(file_path_list)
        csv.register_dialect("myDialect", quoting=csv.QUOTE_ALL, skipinitialspace=True)
        with open(summary_filepath, 'w', encoding='utf8', newline='') as f:
            writer = csv.writer(f, dialect='myDialect')
            writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length', \
                             'level', 'location', 'sessionId', 'song', 'userId'])
            for row in full_data_rows_list:
                if (row[0] == ''):
                    continue
                writer.writerow(
                        (row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
        print(f'{i}/{num_files} files loaded')


def main():
    cluster = Cluster()
    session = cluster.connect()
    session.set_keyspace('udacity')

    process_data('event_datafile_new.csv')
    process_song_library_session(session, 'event_datafile_new.csv')
    process_song_playlist_session(session, 'event_datafile_new.csv')
    process_user_song_history(session, 'event_datafile_new.csv')


if __name__ == '__main__':
    main()
