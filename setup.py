from distutils.core import setup
setup(
  name = 'FinGen',
  packages = ['FinGen'],
  version = '0.3.1',
  license='GPLv3',
  description = 'A penetration testing findings generator using ChatGPT.',
  author = 'Stratus Security',
  author_email = 'contact@stratussecurity.com',
  url = 'https://github.com/Stratus-Security/FinGen',
  keywords = ['ChatGPT', 'Pentesting', 'Penetration Testing', 'Findings Generator'],
  install_requires=[
    'openai'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',
  ],
)