import matplotlib.pyplot as plt
from math import cos, sin


def plot_robot_arm(theta, target, arm_lengths):
    """
        Plots the configuration of a 2-link robotic arm and its target point.

        Parameters:
        -----------
        theta : list or tuple of floats
            The joint angles of the robotic arm in radians.
            theta[0] is the angle of the first segment with the horizontal (x-axis).
            theta[1] is the angle of the second segment with the horizontal (x-axis).

        target : list or tuple of floats
            The target position in the 2D plane as [x, y].

        arm_lengths : list or tuple of floats
            The lengths of the two segments of the robotic arm.
            arm_lengths[0] is the length of the first segment.
            arm_lengths[1] is the length of the second segment.

        Returns:
        --------
        None
            This function does not return any value. It displays a plot of the robotic arm
            and the target point in the 2D plane.

        Description:
        ------------
        This function visualizes the position of a 2-link robotic arm given the joint angles (theta)
        and the lengths of the arm segments. The function calculates the positions of the joints and
        the end effector (the point at the end of the second segment) and then plots the arm segments
        as lines. The target point is also plotted on the same graph to illustrate the difference
        between the arm's end effector position and the desired target position. The plot is set to
        maintain an equal aspect ratio for accurate representation, and grid lines are enabled for
        better visualization.

        Usage:
        ------
        plot_robot_arm([theta1, theta2], [x_target, y_target], [l1, l2])

        Example:
        --------
        plot_robot_arm([0.5, 1.0], [2, 3], [1, 1.5])

        This would plot the robotic arm with:
        - The first segment rotated by 0.5 radians (≈28.65 degrees) from the x-axis.
        - The second segment rotated by an additional 1.0 radians (≈57.30 degrees) relative to the first segment.
        - A target point at coordinates (2, 3) on the 2D plane.
        - The lengths of the two arm segments are 1 and 1.5 units, respectively.
        """

    # Calculate the positions of the joints
    l1, l2 = arm_lengths

    x0, y0 = 0, 0  # Base of the robot arm
    x1 = l1 * cos(theta[0])
    y1 = l1 * sin(theta[0])
    x2 = x1 + l2 * cos(theta[1])
    y2 = y1 + l2 * sin(theta[1])

    # Plot the arm segments
    plt.plot([x0, x1], [y0, y1], 'ro-', label='Segment 1')
    plt.plot([x1, x2], [y1, y2], 'bo-', label='Segment 2')

    # Plot the target point
    plt.plot(target[0], target[1], 'gx', label='Target', markersize=10)

    # Setting up the plot
    plot_max = max(target[0], l1 + l2, target[1])
    plt.xlim(- plot_max - 0.5, plot_max + 0.5)
    plt.ylim(- plot_max - 0.5, plot_max + 0.5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.legend()
    plt.title('Robotic Arm Configuration')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Show the plot
    plt.show()



