import logging
import math


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="/home/damian/test/my.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w")
logger = logging.getLogger()


def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0"""
    logger.info(f'Quadratic formula of: a = {a}, b = {b}, c = {c}')

    # Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return root1, root2


a = int(input("Parameter a = "))
b = int(input("Parameter b = "))
c = int(input("Parameter c = "))

roots = quadratic_formula(a, b, c)
print(roots)
