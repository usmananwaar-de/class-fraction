class Fraction:
    """
    Represents a fraction with a numerator and denominator.

    Attributes:
        num (int): The numerator of the fraction.
        dem (int): The denominator of the fraction.
    """

    def __init__(
        self, num, dem
    ):  # Initializes the Fraction object with numerator and denominator.
        self.num = num
        self.dem = dem

    def __del__(
        self,
    ):  # Destructor method that is called when the Fraction object is deleted from memory.
        print("The values have discarded")

    def __str__(
        self,
    ):  # Returns a string representation of the Fraction object in the form of a fraction.
        return f"{self.num}/{self.dem}"

    def __gt__(
        self, other
    ):  # Compares two Fraction objects and returns True if the first object is greater than the second.
        if self.num * other.dem > self.dem * other.num:
            return True
        else:
            return False

    def __ge__(
        self, other
    ):  # Compares two Fraction objects and returns True if the first object is greater than or equal to the second.
        if self.num * other.dem >= self.dem * other.num:
            return True
        else:
            return False

    def __eq__(
        self, other
    ):  # Compares two Fraction objects and returns True if they are equal.
        if self.num == other.num and self.dem == other.dem:
            return True
        else:
            return False

    def __ne__(
        self, other
    ):  # Compares two Fraction objects and returns True if they are not equal.
        if self.num != other.num and self.dem != other.dem:
            return True
        else:
            return False

    def __add__(
        self, other
    ):  # Adds two Fraction objects and returns the result as a new Fraction object.
        return f"{self.num + other.num}/{self.dem + other.dem}"

    def __sub__(
        self, other
    ):  # Subtracts two Fraction objects and returns the result as a new Fraction object.
        return f"{self.num - other.num}/{self.dem - other.dem}"

    def __mul__(
        self, other
    ):  # Multiplies two Fraction objects and returns the result as a new Fraction object.
        return f"{self.num * other.num}/{self.dem * other.dem}"

    def __truediv__(
        self, other
    ):  # Divides two Fraction objects and returns the result as a new Fraction object.
        total_num = self.num_mult_dem(other)
        total_dem = self.dem_mult_num(other)

        if (
            total_num % total_dem == 0
        ):  # Simplifies the fraction if possible before returning.
            return f"{total_num/total_dem}/{total_dem/total_dem}"
        elif total_dem % total_num == 0:
            return f"{(total_num/total_num)}/{total_dem/total_num}"
        else:
            return f"{total_num}/{total_dem}"

    def __floordiv__(
        self, other
    ):  # Performs floor division on two Fraction objects and returns the result as a new Fraction object.
        total_num = self.num_mult_dem(other)
        total_dem = self.dem_mult_num(other)

        return f"{total_num//total_dem}/{total_dem//total_dem}"

    def num_mult_dem(
        self, other
    ):  # Multiplies numerator of the first Fraction object with denominator of the second Fraction object.
        return self.num * other.dem

    def dem_mult_num(
        self, other
    ):  # Multiplies denominator of the first Fraction object with numerator of the second Fraction object.
        return self.dem * other.num

    def __abs__(self):
        # Returns the absolute value of the fraction
        return f"{abs(self.num)}/{abs(self.dem)}"

    def __int__(self):
        # Returns the integer value of the fraction by performing integer division
        return int(self.num / self.dem)

    def __float__(self):
        # Returns the floating point value of the fraction
        return float(self.num / self.dem)

    def __round__(self, nDigits):
        # Rounds the fraction to nDigits number of decimal places
        return f"{(self.num / self.dem):.{nDigits}f}"

    def __trunc__(self):
        # Truncates the fraction to an integer by truncating the numerator and denominator
        return f"{self.num:.0f}/{self.dem:.0f}"

    def __ceil__(self):
        # Returns the smallest integer greater than or equal to the fraction
        if self.num < 0 and self.dem < 0:
            return f"{self.num:.0f}/{self.dem:.0f}"
        elif self.num < 0:
            return f"{self.num:.0f}/{(self.dem+1):.0f}"
        elif self.dem < 0:
            # Fixes the bug where it doesn't return the value
            return f"{(self.num+1):.0f}/{self.dem:.0f}"
        else:
            return f"{(self.num+1):.0f}/{(self.dem+1):.0f}"

    def __floor__(self):
        # Returns the largest integer less than or equal to the fraction
        if self.num > 0 and self.dem > 0:
            return f"{self.num:.0f}/{self.dem:.0f}"
        elif self.num > 0:
            return f"{self.num:.0f}/{(self.dem-1):.0f}"
        elif self.dem > 0:
            return f"{(self.num-1):.0f}/{self.dem:.0f}"
        else:
            # Fixes the bug where it doesn't return the value
            return f"{(self.num-1):.0f}/{(self.dem-1):.0f}"
