import clusterObject

# Define the Paragraph class that inherits from Cluster
class Paragraph(clusterObject.Cluster):
    def __init__(self, content, xml):
        # Call the __init__ method of the Cluster class
        super().__init__()
        self.content = content
        self.modContent = None
        self.xml = xml
        self.ruleA = []

    def set_parentClusterN(self, new_value):
        self.set_clusterN(new_value)
