from functools import wraps

from allure_commons._allure import StepContext, attach
from allure_commons.types import AttachmentType
from allure_commons.utils import func_parameters, represent


def step(title):
    if callable(title):
        return CustomStepContext(title.__name__, {})(title)
    else:
        return CustomStepContext(title, {})


class CustomStepContext(StepContext):
    def __enter__(self):
        super().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)

    def __call__(self, func):
        @wraps(func)
        def impl(*args, **kwargs):
            f_args = list(map(lambda x: represent(x), args))
            f_params = func_parameters(func, *args, **kwargs)
            with StepContext(self.title.format(*f_args, **f_params), f_params):
                try:
                    step_result = func(*args, **kwargs)
                    return step_result
                finally:
                    attach(
                        args[0].driver.get_screenshot_as_png(),
                        'Screenshot',
                        attachment_type=AttachmentType.PNG,
                    )

        return impl
