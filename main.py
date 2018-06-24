from bs4 import BeautifulSoup
import json
import os

class nodeController:
    def __init__(self, node):
        self.node = node
        self.nodeAttrs = node.attrs

    def getAttr(self, attribute):
        return self.nodeAttrs[attribute] if attribute in self.nodeAttrs else None

functions = []
for root, dirs, files in os.walk('test/'):
    for file in files:
        if file.endswith('.cfc'):
            with open(os.path.join(root, file), "r") as fp:
                print(root)
                print(file)
                soup = BeautifulSoup(fp, 'html.parser')

                for cffunction in soup.find_all('cffunction'):
                    nc = nodeController(cffunction)
                    functions.append({
                        'name': nc.getAttr('name'),
                        'access': nc.getAttr('access'),
                        'returntype': nc.getAttr('returntype'),
                        'hint': nc.getAttr('hint')
                    })
print(json.dumps(functions, indent=2))
