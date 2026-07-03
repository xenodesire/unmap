import textwrap

class WriteBanner:
    @staticmethod
    def banner():
        banner = textwrap.dedent(r"""
        _  _    _  _  _    __,    _  
|   |  / |/ |  / |/ |/ |  /  |  |/ \_
 \_/|_/  |  |_/  |  |  |_/\_/|_/|__/ 
                               /|    
                               \|  
        """)
        print(banner)