class Utils:
    chants_stanzas = {
        'i': 106,
        'ii': 113,
        'iii': 143,
        'iv': 104,
        'v': 100,
        'vi': 99,
        'vii': 87,
        'viii': 99,
        'ix': 95,
        'x': 156
    }

    base_url = 'https://oslusiadas.org/'

    @staticmethod
    def parse_scrapy_response(response_array):
        response_array[0] = ''
        response_array[1] = ''
        array_with_text = list(filter(lambda x: x != "\n", response_array))
        return array_with_text

    def from_roman(self, num):
        num = num.upper()
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(num)):
            if i > 0 and rom_val[num[i]] > rom_val[num[i - 1]]:
                int_val += rom_val[num[i]] - 2 * rom_val[num[i - 1]]
            else:
                int_val += rom_val[num[i]]

        return int_val

    def parse_chant_url(self, url):
        url_params = url[23:]
        array_params = url_params.split('/')

        return {"chant_number": self.from_roman(array_params[0]),
                "stranza": 1 if (array_params[1] == '') else int(array_params[1])}

    def generate_chants_links(self):
        urls = []
        for chant, number_of_chants in self.chants_stanzas.items():
            url_chant = self.base_url + chant + '/'
            urls.append(url_chant)
            for chant_stanza in range(number_of_chants - 1):
                urls.append(url_chant + str(chant_stanza + 2) + '/')

        return urls

