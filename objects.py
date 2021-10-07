import numpy as np

def __triangularization(points, center):

    aux = []
    for i in range(len(points)):
        aux.append(points[i])
        aux.append(points[i])

    points = aux.copy()
    points.pop(0)
    points.pop(len(points)-1)

    for i in range(len(aux), 0, -1):
        if (i%2 == 0) & (i != 0) & (i != len(aux)):
            points.insert(i, center)

    return points

def Planet():
    planet = np.zeros((101,2))
    # preenchendo as coordenadas do pentagrama
    for counter in range(101):
        angle = (2 * np.pi / 100) * counter
        x,y = np.cos(angle),  np.sin(angle)
        planet[counter] = [x,y]
    return planet

def Continent():

    center = (0.1710380932967, -0.3962519254644)

    southAmerica = [
        (0.0579357315266, -0.9068283014548),
        (0.0981462836543, -0.8099458674214),
        (0.1516491169932, -0.7323275147239),
        (0.2584815593625, -0.6716173942614),
        (0.3390758879264, -0.6095306648022),
        (0.3810908878453, -0.5552957236495),
        (0.4848372427153, -0.5458642368432),
        (0.5394286430619, -0.4964283030322),
        (0.5665767950371, -0.4106795926186),
        (0.6460680127308, -0.331622004453),
        (0.5697206239726, -0.2629196326522),
        (0.4424837615447, -0.195899170329),
        (0.3936662035871, -0.1088720148149),
        (0.3087828223298, -0.0648584097185),
        (0.2050364674598, 0.0263126294097),
        (0.0643987236278, 0.0820094900203),
        (-0.1004075749514, -0.0375558638509),
        (-0.1502162022466, -0.1245911594922),
        (-0.0874815907491, -0.2702235794921),
        (0, -0.3639369649587),
        (-0.0519351341928, -0.6321511371562),
        (0, -0.8665347882596),
        (0.0579357315266, -0.9068283014548)]

    continent = __triangularization(southAmerica, center)

    center = (-0.2792724814426, 0.0984019189911)

    centralAmerica = [
        (-0.1451615223118, -0.049582587636),
        (-0.1004075749514, -0.0375558638509),
        (-0.1405370064797, -0.0125864609792),
        (-0.1729086173044, 0.0128483760973),
        (-0.1752208752205, 0.0799038556627),
        (-0.2399640968698, 0.1030264348232),
        (-0.2260905493735, 0.1747064302206),
        (-0.2746479656105, 0.1770186881367),
        (-0.3070195764352, 0.142334819396),
        (-0.3763873139166, 0.144647077312),
        (-0.540557625956, 0.1562083668922),
        (-0.3671382822524, 0.1007141769071),
        (-0.3116440922673, 0.0614057923343),
        (-0.2307150652056, 0.0313464394257),
        (-0.2260905493735, -0.0125864609792),
        (-0.1451615223118, -0.049582587636) ]

    continent += __triangularization(centralAmerica, center)

    center = (-0.3434441034514, 0.5695960790357)

    northAmerica = [
        (-0.3763873139166, 0.144647077312),
        (-0.540557625956, 0.1562083668922),
        (-0.3907647305705, 0.2501818459817),
        (-0.3079536331121, 0.3211627866604),
        (-0.1849200026024, 0.3211627866604),
        (-0.1352333441273, 0.2998685044568),
        (-0.1257692187035, 0.2525478773376),
        (-0.0902787483642, 0.2691100968293),
        (-0.0879127170082, 0.3448231002199),
        (0, 0.4),
        (0.0895396346885, 0.500981169713),
        (0.1534224812993, 0.5246414832725),
        (0.2362335787577, 0.5483017968321),
        (0.3166786448602, 0.5837922671714),
        (0.3143126135042, 0.657139239206),
        (0.4633725889294, 0.6949957409013),
        (0.4, 0.8),
        (0.2835542058768, 0.8558858731063),
        (0.2, 0.8),
        (0.0942716974004, 0.7470484307324),
        (0.0422190075694, 0.7541465248002),
        (-0.0263959017534, 0.7801728697157),
        (0.1250301050278, 0.8842782493778),
        (0.0493171016372, 0.9481610959886),
        (-0.0618863720927, 0.9434290332767),
        (-0.1991161907381, 0.9647233154803),
        (-0.3032215704001, 0.9670893468362),
        (-0.4025948873503, 0.9363309392088),
        (-0.4948701102325, 0.8913763434456),
        (-0.5800472390469, 0.8393236536146),
        (-0.6557602424375, 0.7896369951396),
        (-0.6486621483697, 0.7399503366645),
        (-0.6462961170137, 0.6169167061548),
        (-0.7504014966757, 0.498615138357),
        (-0.7314732458281, 0.4087059468307),
        (-0.6486621483697, 0.3329929434401),
        (-0.5634850195553, 0.1981291561507),
        (-0.3763873139166, 0.144647077312)
        ]

    continent += __triangularization(northAmerica, center)

    return np.array(continent)

# def Continent():
#     continent = [
#         (0.1255581498995, -0.9347072861906),
#         (0.0720809719474, -0.8478068720184),
#         (0.1188735026555, -0.8210682830423),
#         (0.1155311790335, -0.7542218106022),
#         (0.1823776514736, -0.6974023090281),
#         (0.3461515089519, -0.6004749239899),
#         (0.372890097928, -0.5503400696598),
#         (0.4765021302102, -0.5469977460378),
#         (0.5400062790283, -0.4734666263537),
#         (0.5567178971383, -0.4199894484016),
#         (0.6402759876885, -0.3698545940715),
#         (0.6503029585545, -0.3163774161194),
#         (0.5801141624924, -0.2729272090333),
#         (0.4263672758801, -0.1826844712391),
#         (0.399628686904, -0.109153351555),
#         (0.3093859491099, -0.0623608208469),
#         (0.2859896837558, -0.0155682901388),
#         (0.1690083569856, 0.0379088878133),
#         (0.0887925900575, 0.0913860657654),
#         (-0.0515850020668, 0.0679898004113),
#         # (-0.41558312008, 0),
#         (-0.0950352091529, -0.0322799082489),
#         (-0.168566328837, 0),
#         (-0.175250976081, 0.0813590948993),
#         (-0.2320704776551, 0.0947283893874),
#         (-0.2220435067891, 0.1749441563155),
#         (-0.2822053319852, 0.1849711271815),
#         (-0.3089439209613, 0.1381785964735),
#         (-0.3657634225354, 0.1515478909615),
#         (-0.4, 0.2),
#         (-0.3590787752914, 0.2952678067078),
#         (-0.2521244193872, 0.3153217484398),
#         (-0.148512387105, 0.3220063956838),
#         (-0.1217737981289, 0.2651868941097),
#         (-0.0716389437988, 0.2651868941097),
#         (-0.0816659146649, 0.3587719555259),
#         (0, 0.4),
#         (0.1155311790335, 0.5091765185162),
#         (0.2224855349377, 0.5659960200903),
#         (0.3260975672199, 0.5793653145783),
#         (0.2926743309998, 0.6194731980424),
#         (0.3227552435979, 0.6662657287504),
#         (0.39294403966, 0.6528964342624),
#         (0.366205450684, 0.6094462271763),
#         (0.4631328357222, 0.6094462271763),
#         (0.4698174829662, 0.6629234051284),
#         (0.4263672758801, 0.7431391720566),
#         (0.4, 0.8),
#         (0.3327822144639, 0.7899317027647),
#         (0.2960166546219, 0.8400665570948),
#         (0.2, 0.8),
#         (0.1389274443876, 0.7264275539466),
#         (0.0921349136795, 0.6829773468605),
#         (0.0587116774594, 0.7464814956786),
#         (0, 0.8),
#         (0.1121888554115, 0.8701474696928),
#         (0.1990892695837, 0.8701474696928),
#         (0.2525664475358, 0.9269669712669),
#         (0.1322427971435, 0.967074854731),
#         (-0.0215040894687, 0.933651618511),
#         (-0.148512387105, 0.9303092948889),
#         (-0.2287281540331, 0.957047883865),
#         (-0.2788630083632, 0.960390207487),
#         (-0.4025289823775, 0.9169400004009),
#         (-0.4727177784396, 0.8734897933148),
#         (-0.5395642508797, 0.8467512043388),
#         (-0.6298069886739, 0.7865893791427),
#         (-0.6231223414299, 0.7297698775686),
#         (-0.6264646650519, 0.6796350232385),
#         (-0.6298069886739, 0.6027615799323),
#         (-0.67325719576, 0.5459420783582),
#         (-0.7167074028461, 0.4958072240281),
#         (-0.70668043198, 0.4155914571),
#         (-0.676599519382, 0.3721412500139),
#         (-0.6264646650519, 0.2384483051336),
#         (-0.5596181926118, 0.2384483051336),
#         (-0.5328796036357, 0.1448632437175),
#         (-0.3657634225354, 0.0913860657654),
#         (-0.2487820957652, 0.0312242405693),
#         (-0.145170063483, -0.0623608208469),
#         (-0.155197034349, -0.125864969665),
#         (-0.0749812674208, -0.2929811507654),
#         (0, -0.3665122704495),
#         (-0.0148194422247, -0.4634396554877),
#         (-0.0348733839568, -0.5770786586359),
#         (-0.0315310603348, -0.7274832216262),
#         (0, -0.8511491956404)
#     ]
#     return np.array(continent)

def Sun():
    
    sun = np.zeros((101,2))
    # preenchendo as coordenadas do pentagrama
    for counter in range(101):
        angle = (2 * np.pi / 100) * counter
        x,y = np.cos(angle),  np.sin(angle)
        sun[counter] = [x,y]
    return sun

def Moon():
    
    moon = np.zeros((101,2))
    # preenchendo as coordenadas do pentagrama
    for counter in range(101):
        angle = (2 * np.pi / 100) * counter
        x,y = np.cos(angle),  np.sin(angle)
        moon[counter] = [x,y]
    return moon

def Ship():
    ship =  [
    (0.0, +0),
    (+0.05, 0.1),
    (0.05, 0.03),
    (0.1, 0),
    (0.04, 0.06),
    (0.06, 0.06),
    (0.05, 0.07)
    ]
    return np.array(ship)

def Stars():
    stars = 100*(np.random.rand(1000000, 2))-100*(np.random.rand(1000000, 2))
    return np.array(stars)