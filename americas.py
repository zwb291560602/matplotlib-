from pygal_maps_world.maps import World

wm = World()
wm.title = 'North,Central,and South Amercia'
wm.add('North America', {'ca':34126000,'mx':309349000,'us':113423000})
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South Ameirca',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])
wm.render_to_file('americas.svg')
