
# Document Classifier Module
"""Classifies documents into predefined categories based on keyword matching."""

class DocumentClassify:# Document Classifier Using Keyword Matching

    def __init__(self):
        self.categories = {
            'HR': ['employee', 'salary', 'leave', 'attendance'],# Human Resources Keywords
            'Finance': ['invoice', 'bill', 'receipt', 'payment'],# Finance Keywords
            'Operations': ['order', 'delivery', 'shipment', 'inventory'],# Operations Keywords
            'Legal': ['contract', 'agreement', 'dispute', 'lawsuit']# Legal Keywords
        }

    def classifer(self, content):
        content = content.lower()
        count_score  = {}

        for category, keywords in self.categories.items():
            score = 0# Score based on keyword matches
            for keyword in keywords:
                if keyword in content:
                    score += 1
        
            if score > 0:
                count_score[category] = score

        if count_score:
            return max(count_score.items(), key=lambda x: x[1])[0]

        return 'Unknown'

