import pytest
from pyDictStore import storage, default, isDefault,getDefault


def onPropertyChanged(sender, name:str, oldValue, newValue):
    print('standalone onPropertyChanged', name,oldValue,newValue)

@storage
class TestPropDefaul(): 
    def __init__(self) -> None:
        self.PropertyChanged += self.onPropertyChanged
        self.PropertyChanged += onPropertyChanged
              
    @staticmethod
    def onPropertyChanged(sender, name:str, oldValue, newValue):
        print('class onPropertyChanged', name,oldValue,newValue)

    @property
    @default(10)
    def item(self) -> int: ...
    @item.setter
    def item(self,value) -> None: ...

    @property
    def item2(self) -> int: ...
    @item2.setter
    def item2(self,value) -> None: ...

def test_s():
    a = TestPropDefaul()
    a.item = 12

    print('item',a.item)
    print('item Default Value:',getDefault(a,'item'))
    print('item == Default:',isDefault(a,'item'))
    a.item = 10
    print('item',a.item)
    print('item Default Value:',getDefault(a,'item'))
    print('item == Default:',isDefault(a,'item'))

    print('item2:',a.item2)
    print('item2 Default Value:',getDefault(a,'item2'))
    print('item2 == Default:',isDefault(a,'item2'))
    assert(isDefault(a,'item2'))

    print("-----")
    print('TestPropDefaul Default Value:',getDefault(TestPropDefaul(),'item'))
    assert(getDefault(TestPropDefaul(),'item') == 10)

if __name__ == "__main__":
    test_s()