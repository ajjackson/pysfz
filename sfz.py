################################################################################
#                                                                              #
# Copyright 2014 Adam Jackson                                                  #
#                                                                              #
# sfz.py is free software: you can redistribute it and/or modify it under the  #
# terms of the GNU General Public License as published by the Free Software    #
# Foundation, either version 3 of the License, or (at your option) any later   #
# version.  This program is distributed in the hope that it will be useful,    #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General    #
# Public License for more details.  You should have received a copy of the GNU #
# General Public License along with this program.  If not, see                 #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

from collections import OrderedDict

# An ordered dict isn't strictly necessary, but it makes the output
# more predictable.

class Instrument(object):
    """
    Sampler instrument

    Attributes:
        name: string containing instrument name

        regions: List of Region objects

    """
    def __init__(self,regions=False,name=False):

        if regions:
            self.regions = regions
        else:
            self.regions = []

        self.name = name


class Region(object):
    """
    Sample region

    Attributes:
        opcodes: OrderedDict of region properties. Dictionary keys are the
                 same as their corresponding SFZ opcodes.

    """
    def __init__(self,opcodes=False):

        if opcodes:
            self.opcodes = OrderedDict(opcodes)
        else:
    self.opcodes= OrderedDict()


    ### N.B. OrderedDict items are added or modified with the "update" method
