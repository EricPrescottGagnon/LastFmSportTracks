import os
import xml.etree.ElementTree as ElementTree
import pandas


ns = {"tc": "http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2"}


def get_activities(path):
    names = os.listdir(path)

    points = []

    for name in names:
        if name[-4:] == ".tcx":
            print 'file: ' + name
            tree = ElementTree.parse(path + "\\" + name)
            for activity in tree.getroot().find('tc:Activities', ns).findall('tc:Activity', ns):
                for lap in activity.findall('tc:Lap', ns):
                    for track in lap.findall('tc:Track', ns):
                        for trackpoint in track.findall('tc:Trackpoint', ns):
                            tp = manage_trackpoint_element(trackpoint)
                            points.append(tp)

    return pandas.DataFrame(points)


def manage_trackpoint_element(trackpoint_element):
    datetime = trackpoint_element.find('tc:Time', ns).text
    altitude_meters = trackpoint_element.find('tc:AltitudeMeters', ns).text
    distance_meters = trackpoint_element.find('tc:DistanceMeters', ns).text

    return {'datetime': datetime, 'altitude': altitude_meters, 'distance': distance_meters}
