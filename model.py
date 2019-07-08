class wsResultModel:
    def __init__(self):
        self.referenceNumber = ""
        self.fullname = ""
        self.nup = ""
        self.adnid = ""
        self.oldname = ""
        self.documentName = ""
        self.folderName = ""
        self.doctype = ""
        self.subtype = ""
        self.additionalAttribute = ""
        self.additionalMetadata = ""
        self.creationDate = ""
        self.url = ""
    
    def toString(self):
        return self.referenceNumber + ',' + self.fullname + ',' + self.nup + ',' + self.adnid + ',' + self.oldname + ',' + self.documentName + ',' + self.folderName + ',' + self.doctype + ',' + self.subtype + ',' + self.additionalAttribute + ',' + self.additionalMetadata + ',' + self.creationDate + ',' + self.url

class wsRuleModel:
    def __init__(self):
        self.referenceNumber = ""
        self.filename = ""
        self.metadataName = ""
        self.infoMetadata = ""