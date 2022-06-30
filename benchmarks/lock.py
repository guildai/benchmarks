from tempfile import mkdtemp
from guild import lock

class TimeSuite:
    def setup(self):
        self.lock_dir = mkdtemp()
        self.unlocked_lock = lock.Lock("unlocked", timeout=1, guild_home=self.lock_dir)
        self.locked_lock = lock.Lock("locked", timeout=1, guild_home=self.lock_dir)
        self.locked_lock.acquire()

    def time_create(self):
        l = lock.Lock("new_lock", timeout=1, guild_home=self.lock_dir)
    
    def time_acquire(self):
        self.unlocked_lock.acquire()

    def time_release(self):
        self.locked_lock.release()
 
    def time_acquire_conflict(self):
        self.locked_lock.acquire()