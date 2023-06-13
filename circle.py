import matplotlib.pyplot as plt

from geopy.distance import geodesic
from geopy.point import Point

def calculate_endpoint(latitude, longitude, meters, direction):
    start_point = Point(latitude, longitude)

    # Calculate the endpoint using geodesic distance
    endpoint = geodesic(meters=meters).destination(point=start_point, bearing=direction)

    return endpoint.latitude, endpoint.longitude

# def plot_circle(points):
#     # Extract x and y coordinates from the list of points
#     x_coords = [point[0] for point in points]
#     y_coords = [point[1] for point in points]

#     # Plot the circle points
#     plt.plot(x_coords, y_coords, 'ro-', label='Circle')

#     # Set the aspect ratio of the plot
#     plt.axis('equal')

#     # Set the x and y axis labels
#     plt.xlabel('X')
#     plt.ylabel('Y')

#     # Show the legend and the plot
#     plt.legend()
#     plt.show()

def main():

    lat = 41.736703258838745  # Example latitude
    lng = -116.94812195237198 # Example longitude
    distance_meters = 5 # Example distance in meters
    direction = 90  # Example direction (in degrees)

    end_lat, end_lng = calculate_endpoint(lat, lng, distance_meters, direction)
    print(f"Endpoint coordinates: ({end_lat}, {end_lng})")    # plot_circle(x)


if __name__ == '__main__':
    main()




