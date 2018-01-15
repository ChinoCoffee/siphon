import GPy
from numpy import ndarray


class Manifold(object):
    """

    """
    def __init__(self, latent_dim=2):

        self.latent_dim = latent_dim
        self.kernel = GPy.kern.RBF(latent_dim, ARD=True) + GPy.kern.Bias(latent_dim)
        self.X = None

        self.trajectories = []

    def optimize(self):

        model = GPy.models.BayesianGPLVM(self.X, self.latent_dim, kernel=self.kernel, num_inducing=30)
        model.optimize(messages=False, max_iters=5000)

        # [TODO] plotting

    def predict(self):
        raise NotImplementedError


class ViewMapManifold(Manifold):
    pass


class NodeEdgeManifold(Manifold):
    pass


class ArrangementManifold(Manifold):
    pass


class PolylineManifold(Manifold):
    pass


class BezierManifold(Manifold):
    """

    """
    def add(self, bezier):
        # blender bezier -> bezier

    def normalize(self):
        rotation, translation, scale = None, None, None
        self.rotation = rotation
        self.translation = translation
        self.scale = scale

    def optimize(self):
        self.normalize()
        self.model = self.optimize()
