import matplotlib.pyplot as plt  # Importing the necessary module for plotting
from geopy.distance import geodesic  # Importing the geodesic function for distance calculations
from geopy.point import Point  # Importing the Point class for representing geographical points

def calculate_endpoint(latitude, longitude, meters, direction):
    """
    Calculates the endpoint coordinates based on the given latitude, longitude, distance, and direction.

    Args:
        latitude (float): The latitude of the starting point.
        longitude (float): The longitude of the starting point.
        meters (float): The distance in meters.
        direction (float): The direction in degrees.

    Returns:
        Tuple: The latitude and longitude of the endpoint.
    """
    start_point = Point(latitude, longitude)  # Creating a Point object for the starting point
    endpoint = geodesic(meters=meters).destination(point=start_point, bearing=direction)
    # Calculating the endpoint using geodesic distance with the given parameters
    return endpoint.latitude, endpoint.longitude  # Returning the latitude and longitude of the endpoint

def plot_circle(points):
    """
    Plots the circle on a graph.

    Args:
        points (List[Tuple]): A list of points representing the circle.

    Returns:
        None
    """
    x_coords = [point[1] for point in points]  # Extracting the x-coordinates from the list of points
    y_coords = [point[0] for point in points]  # Extracting the y-coordinates from the list of points

    plt.plot(x_coords, y_coords, 'ro-', label='Circle')  # Plotting the circle points
    plt.axis('equal')  # Setting the aspect ratio of the plot to make it circular
    plt.xlabel('Longitude')  # Setting the x-axis label
    plt.ylabel('Latitude')  # Setting the y-axis label
    plt.legend()  # Showing the legend
    plt.show()  # Displaying the plot

def main():
    lat = 41.736703258838745  # Example latitude
    lng = -116.94812195237198  # Example longitude
    distance_meters = 5  # Example distance in meters
    direction = 90  # Example direction (in degrees)

    end_lat, end_lng = calculate_endpoint(lat, lng, distance_meters, direction)
    # Calculating the endpoint coordinates based on the example parameters
    print(f"Endpoint coordinates: ({end_lat}, {end_lng})")  # Printing the endpoint coordinates
    point = [(end_lat, end_lng)]  # Creating a list of the endpoint coordinates
    plot_circle(point)  # Plotting the circle using the endpoint coordinates

if __name__ == '__main__':
    main()
