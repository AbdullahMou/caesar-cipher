from caesar_cipher.caesar_cipher import *
from caesar_cipher import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_encrypt():
    actual=encrypt('it was the best of times, it was the worst of times',3)
    expected='lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv'
    assert actual==expected

def test_decrypt():
    actual=decrypt('lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv',3)
    expected='it was the best of times, it was the worst of times'
    assert actual==expected  

def test_caracters():
    actual=encrypt('it was the best of times,./"',3)
    expected='lw zdv wkh ehvw ri wlphv,./"'
    assert actual==expected  

def test_crack():
    actual=crack('lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv')
    expected='it was the best of times, it was the worst of times'
    assert actual==expected      