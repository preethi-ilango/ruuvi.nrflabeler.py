import main
import mock
import pytest

FICR_BASE = 0x10000000
  


def test_check():
 assert (main.mac2str(FICR_BASE)!=None)


def test_call_quit_ends_the_game():                                       
    """Tests call_quit and confirming ends the session."""                
    with mock.patch('builtins.input', return_value='y'):                  
       pytest_wrapped_exit = pytest.raises(SystemExit)                   
       assert main.check() == pytest_wrapped_exit.type 
