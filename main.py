import lastFm
import pandas

def main():
    lastFmDataFrame = lastFm.get_recent_tracks()
    print lastFmDataFrame.head(20)


if __name__ == '__main__':
    main()