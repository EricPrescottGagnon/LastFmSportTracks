import lastFm
import sport_tracks
import pandas

def main():
    sport_tracks_dataframe = sport_tracks.get_activities("C:\\Users\\Eric\\Dropbox\\Applications\\tapiriik")
    print sport_tracks_dataframe.head(20)
    # lastFmDataFrame = lastFm.get_recent_tracks()
    # print lastFmDataFrame.head(20)


if __name__ == '__main__':
    main()