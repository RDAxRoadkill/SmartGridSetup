import subprocess
import sys

subprocess.call("sudo apt-get update", shell=True)
subprocess.call("sudo apt-get install python-pip", shell=True)

#SSH 
#subprocess.call("mkdir -p -m 700 ~/.ssh")
#subprocess.call("install -m 600 /dev/null ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDIQ4ub0qEgMcFUO6zyGaPcj/B1A5qlXESjBJ4tJRspKg2uhXsZtygdGtpP9c+QoZzYFagD6alzbV9MQldsHrybm/9mvQcm2P10obdWu2wbFNu49kvHlNcjuyLbwlR4+GESM45A0QTPESS2X4kDnhAZP4wwGYDUX6VSoEXjt6vX8CUcI5DMezlHdbLemfe4rIcIY7PoEeJiQE7t3/dTK/JkoJvb4pfDtOP8atvzfe5oV8+jJoPQDu13DpKJLWnGv2C0wNh/N1zs9m1NF4UkeJ00O26/Y5SmQLSbn1ySuxW0K/JCPgy7e+G+NUxUuaY7uUuT7Vakw++J4DxaRXyBbAJcoeZ9Bws09qQES/IZ4rSuGXrE/mPgVzxln40B0as39k3IJ42oNcPM0opRcCs3BVXK5iqszdrGZEJRAOVM6vCxHObdGmJ3CEpXJ93RVro/jz/52LdzHvYYjk+8h+XWV+Qa9LaJl82R6gAlBX/VJWsI++UM7w6GVdhb1dAPVKW7+dwaxwlvQVNXB41SrH7jpHFZ9d2/YWquF5QIaGP04SNQilQubx1KHE+Wv1WNktASzlZU1gb4qzN65rSzl8O4nlSQCOkd+PUlju6JPIwR1UZgtsHwCRfKGrDXoZdkTKgti1PrU0+YL19/5HqCbGCnzd7VlGIU6GahMGLoT1YAbhDOeQ== wouter@MSI-W" > ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDwaMb4S11fVcOKcWkZbSoYPYvFV9uKOETZjFnmRqokKAYJtwOwdFuMykT/wRs+sU5jNFg0mX07OTLSIoSfy67BuWtJA4RrLYTRNlZUbBf9aPfnUxvx9Pbz/0TRmTELHZ+5RlEXg5m/VSCBbzMG10gLkWTwPGA3K1E+ul0xLQB0CHgiBF88HPa/USek3S8BSTObFaQG++LdaIzpq0vLVoRhMcBQR8+LgqQrTfz3Ko6MeLgaadMGRm6+sxWjej9g2va6GR9RE8j3RQFcSLC4NFAWRwW6Ucac0UY/Yr8Yp/Fslhf5vricupgpFcFzVn0SG2Yd14N2yYa/J0E8N0pH3nnDGXDJuxkRe4w3C9/oDZ5rHJFKCXovy5a303iH2dfbKEPN8DBTdP1HwWCjVYEZw1QYo8+gExiweaoz3nEOFD6qsb6ixoPkvBg4RMJvMOub8kbsFLGazDzG9Y9v7fdQ27a5jRwBqvXYQ+QWumJWBz0di5KVGO9srit7hMVPqIYKOFhN2jlpZGyb+j43jjUOS10B9ya7VBmALAvJXBbN7yEYKXLy5L+VZpnClyeGaRKWpqTX8aCmnF3k41S4YOdBdyViJFP+5i14bdS8etI9i8VRVCm3yiMldKLwxYSoGCgU3ht0/9BWzCd7F1genfDt5Bvy63az+p3sOJxHrbv76tRU6Q== snick@Laptop-Sam" > ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDa/IdYqbqWhwiQvjFvUFs9R5DvhZ7Xg7p5jtYIbvM7KG7iqROf0yw3hkxkbUgTZiclzwQA9T8OI1jQCZV85RpltA3ZkvfcPo/GPSaBx+ilB62wEeEAnP3AVg5zN9FVRcmw/pXrD/dex4vEohaF/Fbf165tCzWUpFtlXijHE+wib6F9qZ3NHPGPesT9B8mRgnKn1ywHK/OaoNnUCgZOcq1Ct0roEUrzHe/lkEvetAWuB3BWHyXJx0wGECmBG1pIuk6VAbJidlImsyNx3kj9v3ESm4gb/o3qYJzoDEh5KJhluIACNzAvQoNTTiublhxSc2UlFjSdnEOm4mvpanpnUPNDPdw3FbeV0xBpt17BsHGJdV0AXJkyCPJGiXPKyoGQzJfTzopBk/+QV77ERDfm71yXCl/PhXalg/YwPTjzxryYgmw3erfi8X+J5DTwtHbhvtn75p8Uv72HBHh4Qo1BXM+lp75uLcDBQfUAHQRhzIv3vN2JqGBFa0f6FcSX7zVh5TXZ5oHigVsaV+ECRFyxMg6KvWIoRK+Dt7XG5GHcT7l+ZNSEjFKaWfW0GQ1/7SuKurl6jPt8qmEsOmpZGN3bIMTLaB0hkhFepyuvrjmaT/myCd86nDVLxNk8ZAE3z4Y4Bu2yqCJ+eglPVTyRL9DrTIgT8vtv7V6iKuhYiXlFGEub7w== kevin quist@MSI" > ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCfbs3FbFFPhDR5v2KhRXCyQZ/cKW5+YZ7EmeSHKCn/lB6RfFhjvdA9KkTS1aPh5JFTUIxG53fQ5F4LADDyKe3VT5sqFZNsIIVvxM1Sjoc5JXLizF6qipNDi95Htsp+I7ol/51AbbCT3n6rVPt7/mK03QR5nOpxVJRoOwjN6/11T+ioiB263DpqoztMKKEfsK7HNJWWOUQBnHDSs9azmKOhgnrfBzxKyfG+XCuLUwcTRdXnl0hVd2P+8R+OdyOlEkeNmSc//l51OSZiamxyRB45f3jNSHe8L9c8zkqzsMGkz/5QxP+cvXJDf9VGOrnAL4tIB/OvUA0ZvHeQ15bU6Xpb5UCQNYPK+Lbq4hopY1FCFfESE4jKYABRdGueFfLnppjuITQQGeN69V2PnpRGunBBZbCf/h1tjHtDbHL1vkKR77w9speTmUqAgy3lrmexgeNjebix7+7pcNRrcAvavWok+YLfwXllhuxfo09Nf9sKJdPoy6JVWxiiID9Bc1ZdGizCKKUk4rzTVGXENdaohDNJfnRiJ05he1q73JEmmIo5Wsj/bUv8iTd8h1eHo0b00zeC+VWzQSxQjSBKCLYRiFRBYbBMyQxiJI8Q912Eik+LgI90qK68ur/aBwhepAfzqn0r8i2e4i7eZ2Luad309LbdssDH6Ass/oV7Dm+NGs5Btw== jacco@DESKTOP-R2ORD65" > ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDfA+K48prAHzrf3CQ/SNf9vjP5aZXj4yeOwS7jVcRAqGXwBta94qnheg6YWVLJpE9NlR3BaXJ+h9SV6kKmWSzUHiuZeGVEgQjlKEL5jW/mhm7pt3p9nVf3ijl6onPHYHaZdq31497kIEWr9uflgbsLMssIDmFg2KG9u0kdNTShhvuzsnt0K2wjl9R06xScWgYOJIRgFHYwYMvTcPZLETMy/Laodt+0kRypGbWZOABo4iPNKwJa035eRs1t2uGUCpRlSBvC1jts9yxt4aSo+k/q4DueWzjXs5uhLPVSe1q/Mu0muKG2Z2tyvvChjsZNLAiRrhXB1v58FteEItKQnw3E+iXNBXQkpgnsRvgGgCkNqwYWhKucvCbCZTLS3gGiSMTsNFsLiqWxRIxe+XR+16H5QKhweHyfFXU4XRcx2YG0v2HTKITNhp0zS1pQ3DkOSUXKBKPeklAoxZGptfrHfSjeuyY4ok4HqB599LPI8ehslOWICF9bhZVhuW+RA0+XR4EgoZBBPYhPTMU/6N2gjeEQ3gOg3ddTdV56lUidz0zbslq1hNWQTAHoxjFDCHqpZaSoDNAfY/VCvzt7tfUJpQmvqEWDRZmMGhDNDwisuO/mKfEI8gvFDig/Yp+IGVUcA8hOE+X8fV6dMp3rRLuUAcf1SadOYSmi/DM0OF9RC0DG5Q== ricky@MSI" > ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCfd9Iq44zIP83AUnebCZDZVz5E/LrnZ1F+Bg6uvbjAgEt4w1aF7/SjU+sy70MTCx0YT2UVIjmNiZZhW80AOIj30CfrCwNTEyd0knrt21gmuUVZocBw/h51h8RzXhAMFS68OU6986Kl3BZ+9AxeL2CedznZ8hZY0GArwnT6YtoVF7RxbbYM9QayStUGPA8rcIBRg05xoq/lPSm0YrGqhVz3jwNds93FsBlNSiWFfGP64uqbW9Hc+uNfWI/EJVpzMX6Tr/BlZQo4dlawyhyLnfZ/EfnynpJCMTrzBTWhx6NWHSPdh5/ChJB6IhdFPE38T3QfFSrwrGwBx+59ecAgyLwhYmERSf31glFbnC7Emdg82VSV0uKhOSPF7/rAfR+CpldI+4bnYofQAIJUH4VbMzIrjlqGEXTxbQPIGCi4xTxEZ0Nzf6NWE2JkHquHfVGuhw1fC1t4woU4kzKXcr4xdGMzlL5pWNfJ5KlBmkPStKQvKM5To6GdXfhHwufGBECTiR8Ts//rtzniLITz23DFb9kZAEerUhvDAr7kQY271rb+qDtTwGMb45ZTE8wwuWViLYf/uA1GHRF0LawSnIKZdvX47iPFjIuasW1uS6BqnfI0+SLpBVLTfcK39j+MMfqqmHzavRICnX9nGVDORN3yo+/asDh3sL9QLV8LKxXhNRNIPQ== jussi@DESKTOP-76OL39A" > ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCmn7QUMNafoMisO17RnGG6lrQPozG1BynemAgzNl+MDHRdHocR6O10ow0uPW8due798Gc1jfIzXS03o6JPrWNAUTgHCtHhm48SoWwc+nzc7g6XJWsMXRRvjtJJllVgaQ5lA33Z3iN8vTxb8T3jOS7WZAkvKSueZgrkuj1BOQWb/fdWaJfs8jF3DUiTUiWAY1URTbF11ig80tJ0THo6ZoSiSIqdZnr47kQw3qYuAFjjlpqxm/UO4OKdmv5nWdvit8uyR2r+a8N+cgGi4/PHG9EYHY5RNpnS7RuEoC4hnU41dAusXKxXogjJVQmGbmDK4iQUe5Feuv1zUVPruWRhK+tp+QE+ijiHJ5szweRmhn2tejhJW3/ei898BPH35G6cJ5LpXYLf21CpBkViPzArXUdhs60NnBJcVbJHXltOsWtC7KJsfuFZ2fubky6v+RZY1/kPxcQ/48z4AHlVs2Ssj4rptOuwoC27v+cgUw5mOZOkBHYZ8PAwZHFZzDckqqTkf5Bu4C9zztGTJVVoea6eInIcrghAND9RQwe1UIKcVpdViA5JYLqZjuaxGlxkC1H7y6dc+n47pOYeRUbKSngrIANLT1Gs2UN45Ge0TvD3TwlyAfpgs2X9kXNUYKS7GQcYxM1WKZovhR2afz1zmJeKYrldWXqyk70NYoHCm7+wrnbgHQ== snick@DESKTOP-SAM" > ~/.ssh/authorized_keys")
#subprocess.call("echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDBmxWTFy9gk74AtcE6ozuThbgL0m36O//IBVSRguDfJTmWbyfI3aWpr6RhShgHFI6IBBymx4k1e8aEjWlGBZepMi3GY0qzTtcc7tnlAr8ugBBmchSOk6m+16KBa5lRQjhc6Pvv5vZVIl5qFPQODbAm9UamM0RG/JKSZtpHmHoiW599qybm4YDWryNhUBpLeaPa1P2UHbighs/bsX97Pr/P5VZWF/cAtBE54hX8cS5x3ZxXClCnbemguuVyI6k/508v/GaIMzfTWit5KWW4lHiLTTt+KifIsBZohKtACMibnPnI/BcXhoEWZ1oKoSoFTwEkE9SyQH7YMd7FHRYuVdfKwRt155xni9+9CGmxxUhgUXSazPmy0a53rvbEZRiR5T0QrDC4MW8aC6epWEqv9I1+CWe7XW9zwmCICz6X9M0Lg07xCMN4oYmWtVlMCkRnxLCTMCbFF/GD11IXrExw8Bws0YE1EET5R2RN1Q3f2neofHdNkIawnZ5K7vIyXvL9Gf3S9wOeg3RQg5l3SN5FIA6CpKB9MnyJQQNcIerH9Xj149xLS/su0661EAkwgi6b7fD7J8TE9EUhyL9zEEJwW2SmNPGZJmGpXdV/sR9sDdjQVzNbsyJPsbdhC17whV3pQCDd+hHpsFnYL9sYq7stKcEoVt0VV2sjoJ2Xa+AMcWLBlQ== sam@sam-laptop" > ~/.ssh/authorized_keys")

import subprocess
import sys

subprocess.call("sudo apt-get update", shell=True)
subprocess.call("sudo apt-get install python-pip", shell=True)
#TensorFlow
subprocess.call("sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev", shell=True)
subprocess.call("sudo apt-get install python3-pip", shell=True)
subprocess.call("pip3 install --user pip", shell=True)

#Python packages
subprocess.call("sudo pip3 install -U numpy==1.16.1", shell=True)
subprocess.call("pip3 install --user future==0.17.1", shell=True)
subprocess.call("pip3 install --user mock==3.0.5", shell=True)
subprocess.call("pip3 install --user h5py==2.9.0", shell=True)
subprocess.call("pip3 install --user keras_preprocessing==1.0.5", shell=True)
subprocess.call("pip3 install --user keras_applications==1.0.6", shell=True)
subprocess.call("pip3 install --user enum34", shell=True)
subprocess.call("pip3 install --user futures", shell=True)
subprocess.call("pip3 install --user testresources", shell=True)
subprocess.call("pip3 install --user setuptools", shell=True)
subprocess.call("pip3 install --user protobuf", shell=True)

subprocess.call('pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu', shell=True)
#Update & Remove
subprocess.call('sudo apt-get dist-upgrade', shell=True)
subprocess.call("sudo apt autoremove", shell=True)
#OpenAI Dependencies
subprocess.call("sudo pip install --user --no-dependencies pyglet==1.3.2", shell=True)
#OpenAI Gym
subprocess.call('sudo pip install --user --no-dependencies gym', shell=True)

#Weights&Biases
subprocess.call('pip install --user wandb', shell=True)
