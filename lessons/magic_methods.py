class Profile:

    handle: str
    followers: int
    private: bool

    def __init__(self, handle: str, followers: int = 0, private: bool = False):
        self.handle = handle
        self.followers = followers
        self.private = private
    
    def __str__(self):
        return f"Handle: {self.handle}\nFollowers: {self.followers}\nPrivate: {self.private}"
    
    def __add__(self, num: float):
        more_followers: Profile = Profile(self.handle, self.followers + num)
        return more_followers



prateek: Profile = Profile("pratnation", private=True)
namith: Profile = Profile("namnam", 500, True)
print(prateek)
print()

namith = namith + 75
print(namith)
print()

prateek = prateek + 299
print(prateek)