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

import re
from collections import OrderedDict

# An ordered dict isn't strictly necessary, but it makes the output
# more predictable.

#TODO(AJJ): clean comments and pre-region space from file before importing
#  regions

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

    def read(self,filename):

        with open(filename,'r') as f:
            file_content = f.read()
        self.regions = []
        for region in file_content.split('<region>'):
            self.regions.append(Region(opcodes=_get_opcodes(region)))

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


def _get_opcodes(region):
    """
    Internal function _get_opcodes from file input.

    Arguments:
        "region" is a string, possibly containing newlines, of text between two
        "<region>" tags from an input .sfz file

    """
    # Get tags with regex: tags don't contain whitespace and are immediately
    # followed by an 'equals' sign
    tags=re.findall('([A-Za-z0-9_.\-]+)(?==)',region)

    # Get values with regex. "Split" serves a nice dual purpose in getting rid
    # of the unwanted characters. List slicing removes empty space before the
    # first tag.
    values=re.split('[A-Za-z0-9_.\-]+=',region)[1:]
    clean_values = [value.strip() for value in values]
    
    # Combine tags and values to form a neat single object
    opcodes_dict = OrderedDict(zip(tags,clean_values))
    
    return opcodes_dict
