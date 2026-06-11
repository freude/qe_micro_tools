from pathlib import Path
import config
import xmlschema
from xml.etree import ElementTree


def xml2dict(path):

    base_dir = Path(__file__).resolve().parent
    config_path = base_dir / "config.cfg"
    cfg = config.Config(str(config_path))

    data = ElementTree.parse(path).getroot()
    qes = data.items()[0][1].split()[1].split('/')[-1].split('.')[0]
    schema = xmlschema.XMLSchema(cfg[qes])
    data_dict = schema.to_dict(data)

    return data_dict


if __name__=='__main__':

    path='/Users/mykhailoklymenko/data-file-schema.xml'

    print(xml2dict(path))