# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor, Input, Path
import os


class Predictor(BasePredictor):
    def setup(self):
        """Load the model into memory to make running multiple predictions efficient"""
        # self.model = torch.load("./weights.pth")

    def predict(
        self,
        video_path: Path = Input(description="Input video"),
        scale: float = Input(
            description="Factor to scale image by", ge=0, le=10, default=1.5
        ),
    ) -> Path:
        """Run a single prediction on the model"""
        generate_vid = "python entry.py --video_name {}".format(video_path)
        os.system(generate_vid)

        video_name = video_path.split("/")[-1]
        video_name = video_name.split(".")[0]

        return "./data/test/{}/output.mp4".format(video_name)
        # processed_input = preprocess(image)
        # output = self.model(processed_image, scale)
        # return postprocess(output)
