class Person:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Weber, Brian')
        self.email = kwargs.get('email', 'brianweber2@gmail.com')
        self.phone = kwargs.get('phone', '941-779-7920')
        self.job = kwargs.get('job', 'Python Devepoler, OWD')
        self.twitter = kwargs.get('twitter', '@brianweber21')
        
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __str__(self):
        return """
            Name:{}
            Email: {}
            Phone: {}
            Job and Company: {}
            Twitter: {}
        """.format(self.name,
                   self.email,
                   self.phone,
                   self.job,
                   self.twitter)