import main
import mock
import pytest

FICR_BASE = 0x10000000
  


def test_check():
 assert (main.mac2str(FICR_BASE)!=None)

 
