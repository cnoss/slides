exports.render = function (data) {
  const { raw, rendered } = this.markdownWithRaw(data);
  console.log('Raw content:', raw);
};
