
import aircv as ac

from common.tools import get_project_path, sep


class FindImg:
    def img_imread(self, img_path):
        return ac.imread(img_path)

    def get_confidence(self, source_path, search_path):
        img_src = self.img_imread(source_path)
        img_sch = self.img_imread(search_path)
        result = ac.find_template(img_src, img_sch)
        print(result)
        return result['confidence']

if __name__ == "__main__":
    source_path = get_project_path() + sep(["img", "src.jpg"], add_sep_before=True)
    search_path = get_project_path() + sep(["img", "head_img.jpg"], add_sep_before=True)
    FindImg().get_confidence(source_path, search_path)