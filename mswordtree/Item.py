import json
from json import JSONEncoder
import uuid 


class Item(JSONEncoder):

    def __init__(self):
        self.GUID = str(uuid.uuid4())
        self.Type = ''        
        self.Content = ''
        self.N = None
        self.Parent = None
        self.Items = []
    
    
    def GetSubHeadings(self):
        heads = list(filter(lambda item: 'Heading' in item.Type, self.Items))
        items = []
        for index, head in enumerate(heads):
            if index == 0:                
                continue    # reason we're ignoring the first element because it is redundant heading i.e (head == subhead)
            items.append(head)
        return items   
    
    def GetTables(self):
        return list(filter(lambda item: 'Table' in item.Type, self.Items))

    def GetParagraph(self):
        return list(filter(lambda item: 'Heading' not in item.Type, self.Items))
    
    def GetChildren(self):
        return self.Items
    
    def GetChild(self, guid):
        return next((item for item in self.Items if item.GUID == guid), None)
    
    def toJSON(self):
        return json.dumps(self, default=lambda obj: obj.__dict__)







