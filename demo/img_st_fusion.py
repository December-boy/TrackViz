import shutil

from feature.top10distribution import get_predict_tracks, store_sorted_deltas
from post_process.predict_eval import eval_on_train_test
from profile.fusion_param import get_fusion_param
from train.st_filter import cross_st_img_ranker


# need to run on src directory
def img_st_fusion():
    # pick predict tracks into different class file
    fusion_param = get_fusion_param()
    get_predict_tracks(fusion_param)
    # get distribution sorted list for probability compute
    store_sorted_deltas(fusion_param)

    # merge visual probability and track distribution probability
    cross_st_img_ranker(fusion_param)

    # evaluate
    eval_on_train_test(fusion_param)


def retrain_fusion():
    fusion_param = get_fusion_param()
    shutil.copy(fusion_param['src_distribution_pickle_path'], fusion_param['distribution_pickle_path'])
    # merge visual probability and track distribution probability
    cross_st_img_ranker(fusion_param)

    # evaluate
    eval_on_train_test(fusion_param)


if __name__ == '__main__':
    img_st_fusion()
    retrain_fusion()
