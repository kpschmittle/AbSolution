import click

class DependentlyRequiredOption(click.Option):
    DEPENDEE_VALUES = tuple()
    DEPENDEE_NAME = ''

    def process_value(self, ctx, value):
        value = super().process_value(ctx, value)
        dependee_value = ctx.params[self.DEPENDEE_NAME]
        if value is None and dependee_value in self.DEPENDEE_VALUES:
            msg = f'Required if --{self.DEPENDEE_NAME}={dependee_value}'
            raise click.MissingParameter(ctx=ctx, param=self, message=msg)
        return value

