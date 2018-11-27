# encoding: utf-8
import unittest
import sys
from bs4 import BeautifulSoup
sys.path.insert(0, "/home/suporte/ProjMacrofitas/src/scrapping")
from speciesLink import parseDiv

class TestParserDivValid(unittest.TestCase):
    def setUp(self):
        mockFile = open("mock.html", 'w')
        mockContent = """
            <div class="record" id="record_99"><table border="0" width="100%"><tr id="detail_99" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=EAC" target="manager"><img align="right" src="logos/institutions/UFC.gif" width="50px"/></a></td>
            <td><span onclick="top.getDetail(900090919,99)">
            <span class="tK">Plantae</span> <span class="tF">Acanthaceae</span> <br/> <span class="tGa"> <u>Dicliptera</u> </span> <span class="tEa"> <u>ciliaris</u> </span> <span class="tA">Juss.</span>. <ll>Det: </ll> <span class="tI">Loiola, M.I.B.; Nunes, E.</span> <span class="tY">04/10/2010</span><br/> <span class="tN">EAC 48786</span> <ll>Coleta: </ll> <span class="cL">Vaz da Silva, I.H.C.V.</span> <span class="cN">45</span> <span class="cY">28/06/2010</span>. <br/> <ll>Loc: </ll> <span class="lP">Serra das Almas.</span>, <span class="lM">Crateús</span>, <span class="lS">Ceará</span>, <span class="lC">Brasil</span> <ll>Cód. barras: </ll> <span class="bC">EAC0048786.</span> <br/> <ll>Coord. munic.:  </ll> <span class="lA">[<i>lat: </i>-5.1783299446106</span> <span class="lO"> <i>long: </i>-40.6775016784668</span> <span class="eR"> <i>err: </i>±43216</span> WGS84]<br/> <ll>Notas:</ll> <no>Erva; terófito; flor lilás. Material de banco de sementes de solo coletado em dezembro de 2009.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário Prisco Bezerra (EAC)</span></td></tr></table>
            </td>
            <td align="right"><table><tr><td valign="top" width="50px"><a class="highslide" href="http://reflora.cria.org.br/inct/exsiccatae/image/imagecode/EAC0048786/size/huge/format/jpeg/foo/19072" onclick="return top.hs.expand(this, { slideshowGroup: 99 }, { bc: 'EAC0048786' })"><img align="right" alt='&lt;table width="100%"&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;Herbário Prisco Bezerra [&lt;a href="downImage?imagecode=EAC0048786"&gt;EAC0048786&lt;/a&gt;]&lt;/b&gt;&lt;/td&gt;&lt;td
            align="right"&gt;&lt;a href="http://reflora.cria.org.br/inct/exsiccatae/viewer/imagecode//EAC0048786/format/slide/initialimagecode/EAC0048786/foo/19072"
            target="other" class="oV"&gt;&lt;big&gt;abrir no &lt;/big&gt;  &lt;img src="imgs/eh.png" height="15px"&gt;&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;
            ' onload="this.style.visibility='visible'" src="http://reflora.cria.org.br/inct/exsiccatae/image/imagecode/EAC0048786/size/thumb/format/jpeg/foo/19072" style="box-shadow: 3px 3px 3px #CCCCCC; border-radius: 5px; visibility: hidden" title="Herbário Prisco Bezerra [EAC0048786]"/></a>
            <div class="highslide-caption"><small><span class="tK">Plantae</span> <span class="tF">Acanthaceae</span> <br/> <span class="tGa"> <u>Dicliptera</u> </span> <span class="tEa"> <u>ciliaris</u> </span> <span class="tA">Juss.</span>. <ll>Det: </ll> <span class="tI">Loiola, M.I.B.; Nunes, E.</span> <span class="tY">04/10/2010</span></small></div>
            </td>
            <td rowspan="2" valign="top" width="21px"><a href="http://reflora.cria.org.br/inct/exsiccatae/viewer/imagecode//EAC0048786/format/slide/foo/19072" target="other" title="abrir no visualizador exsiccatae"><img align="right" height="50px" src="imgs/e.png"/></a></td>
            </tr></table></td></tr></table></div>
            """
        mockFile.write(mockContent)

    def test_parseDiv(self):
        div = BeautifulSoup(open('mock.html'), "html.parser")
        scientificName, municipality, state, country, latitude, longitude, date = parseDiv(div)
        self.assertEqual((scientificName, municipality, state, country, latitude, longitude, date), ("Dicliptera ciliaris", "Crateús", "Ceará", "Brasil", "-5.1783299446106", "-40.6775016784668", "28/06/2010") )

class TestParserDivValid2MissingData(unittest.TestCase):
    def setUp(self):
        mockFile = open("mock2.html", 'w')
        mockContent = """
            <div class="record" id="record_9"><table border="0" width="100%"><tr id="detail_9" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=G" target="manager"><img align="right" src="logos/collections/G.gif" width="50px"/></a></td>
            <td><span onclick="top.getDetail(368261783,9)">
            <span class="tK">Plantae</span> <span class="tF">Acanthaceae</span> <br/> <span class="tGa"> <u>Dicliptera</u> </span> <span class="tEa"> <u>ciliaris</u> </span> <span class="tA">Juss.</span>. <ll>Det: </ll> <span class="tI">Wasshausen, D. C.</span> <span class="tY">01/01/1993</span><br/> <span class="tN">G00082057</span> <ll>Coleta: </ll> <span class="cL">Blanchet, J. S.</span> <span class="cN">646</span> <br/> <ll>Loc: </ll> <span class="lS">Bahia</span>, <span class="lC">Brazil</span> <ll>Cód. barras: </ll> <span class="bC">G00082057.</span> <br/> <ll>Coord. orig.:  </ll> <span class="lA">[<i>lat: </i>-12.1830556</span> <span class="lO"> <i>long: </i>-41.9972222</span> WGS84]<br/> <ll>Notas:</ll> <no>Coordinate uncertainty: No information Image URL: http://www.ville-ge.ch/musinfo/bd/cjb/chg/adetail.php?id=142615&amp;base=img&amp;lang=en</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Geneva Herbaria Catalogue with species Brazil (G)</span></td></tr></table>
            </td>
            <td align="right"><table><tr><td valign="top" width="50px"><a class="highslide" href="http://reflora.cria.org.br/inct/exsiccatae/image/imagecode/G00082057/size/huge/format/jpeg/foo/19072" onclick="return top.hs.expand(this, { slideshowGroup: 9 }, { bc: 'G00082057' })"><img align="right" alt='&lt;table width="100%"&gt;&lt;tr&gt;&lt;td&gt;&lt;b&gt;Conservatoire et Jardin botaniques de la Ville de Genève [&lt;a href="downImage?imagecode=G00082057"&gt;G00082057&lt;/a&gt;]&lt;/b&gt;&lt;/td&gt;&lt;td
            align="right"&gt;&lt;a href="http://reflora.cria.org.br/inct/exsiccatae/viewer/imagecode//G00082057/format/slide/initialimagecode/G00082057/foo/19072"
            target="other" class="oV"&gt;&lt;big&gt;abrir no &lt;/big&gt;  &lt;img src="imgs/eh.png" height="15px"&gt;&lt;/a&gt;&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;
            ' onload="this.style.visibility='visible'" src="http://reflora.cria.org.br/inct/exsiccatae/image/imagecode/G00082057/size/thumb/format/jpeg/foo/19072" style="box-shadow: 3px 3px 3px #CCCCCC; border-radius: 5px; visibility: hidden" title="Conservatoire et Jardin botaniques de la Ville de Genève [G00082057]"/></a>
            <div class="highslide-caption"><small><span class="tK">Plantae</span> <span class="tF">Acanthaceae</span> <br/> <span class="tGa"> <u>Dicliptera</u> </span> <span class="tEa"> <u>ciliaris</u> </span> <span class="tA">Juss.</span>. <ll>Det: </ll> <span class="tI">Wasshausen, D. C.</span> <span class="tY">01/01/1993</span></small></div>
            </td>
            <td rowspan="2" valign="top" width="21px"><a href="http://reflora.cria.org.br/inct/exsiccatae/viewer/imagecode//G00082057/format/slide/foo/19072" target="other" title="abrir no visualizador exsiccatae"><img align="right" height="50px" src="imgs/e.png"/></a></td>
            </tr></table></td></tr></table></div>
            """
        mockFile.write(mockContent)

    def test_parseDiv(self):
        div = BeautifulSoup(open('mock2.html'), "html.parser")
        scientificName, municipality, state, country, latitude, longitude, date = parseDiv(div)
        self.assertEqual((scientificName, municipality, state, country, latitude, longitude, date), ("Dicliptera ciliaris", "", "Bahia", "Brazil", "-12.1830556", "-41.9972222", "") )


class TestParserDivValid3(unittest.TestCase):
    def setUp(self):
        mockFile = open("mock3.html", 'w')
        mockContent = """
            <div class="record" id="record_98"><table border="0" width="100%"><tr id="detail_98" valign="top"><td class="collID"><a href="http://splink.cria.org.br/manager/detail?setlang=pt&amp;resource=HCF" target="manager"><img align="right" src="logos/collections/HCF.jpg" width="50px"/></a></td>
            <td><span onclick="top.getDetail(897495858,98)">
            <span class="tK">Plantae</span> <span class="tF">Acanthaceae</span> <br/> <span class="tGa"> <u>Hygrophila</u> </span> <span class="tEa"> <u>costata</u> </span> <span class="tA">Nees</span>. <ll>Det: </ll> <span class="tI">M.G. Caxambu</span> <span class="tY">17/06/2004</span><br/> <span class="tN">HCF 1000</span> <ll>Coleta: </ll> <span class="cL">E. Ferreira</span> <span class="cY">27/03/2004</span>. <br/> <ll>Loc: </ll> <span class="lP">rio do Campo</span>, <span class="lM">Campo Mourão</span>, <span class="lS">PR</span>, <span class="lC">Brasil</span> <br/> <ll>Coord. munic.:  </ll> <span class="lA">[<i>lat: </i>-24.0456008911133</span> <span class="lO"> <i>long: </i>-52.3830986022949</span> <span class="eR"> <i>err: </i>±28572</span> WGS84]<br/> <ll>Notas:</ll> <no>planta herbácea, ereta, com inflorescências terminais de cor alaranjada.</no><br/><ll>Tipo de registro: </ll> espécime preservado<br/></span>
            <table border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td><span id="credit">© Herbário da Universidade Tecnológica Federal do Paraná Campus Campo Mourão (HCF)</span></td></tr></table>
            </td>
            </tr></table></div>
            """
        mockFile.write(mockContent)

    def test_parseDiv(self):
        div = BeautifulSoup(open('mock3.html'), "html.parser")
        scientificName, municipality, state, country, latitude, longitude, date = parseDiv(div)
        self.assertEqual((scientificName, municipality, state, country, latitude, longitude, date), ("Hygrophila costata", "Campo Mourão", "PR", "Brasil", "-24.0456008911133", "-52.3830986022949", "27/03/2004") )

class TestParserDivInvalid(unittest.TestCase):
    def setUp(self):
        mockFile = open("mock4.html", 'w')
        mockContent = ""
        mockFile.write(mockContent)

    def test_parseDiv(self):
        div = BeautifulSoup(open('mock4.html'), "html.parser")
        scientificName, municipality, state, country, latitude, longitude, date = parseDiv(div)
        self.assertEqual((scientificName, municipality, state, country, latitude, longitude, date), ("", "", "", "", "", "", "") )



if __name__ == '__main__':
    unittest.main()