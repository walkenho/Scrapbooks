```python
tf.boolean_mask(
    tensor,
    mask,
    name='boolean_mask',
    axis=None
)
```


tf.gather(
    params,
    indices,
    validate_indices=None,
    name=None,
    axis=0
)
Gather slices from params axis axis according to indices [manual](https://www.tensorflow.org/api_docs/python/tf/gather)



tf.image.non_max_suppression(
    boxes,
    scores,
    max_output_size,
    iou_threshold=0.5,
    score_threshold=float('-inf'),
    name=None
)
https://www.tensorflow.org/api_docs/python/tf/image/non_max_suppression

Greedily selects a subset of bounding boxes in descending order of score.

Prunes away boxes that have high intersection-over-union (IOU) overlap with previously selected boxes. Bounding boxes are supplied as [y1, x1, y2, x2], where (y1, x1) and (y2, x2) are the coordinates of any diagonal pair of box corners and the coordinates can be provided as normalized (i.e., lying in the interval [0, 1]) or absolute. Note that this algorithm is agnostic to where the origin is in the coordinate system. Note that this algorithm is invariant to orthogonal transformations and translations of the coordinate system; thus translating or reflections of the coordinate system result in the same boxes being selected by the algorithm. The output of this operation is a set of integers indexing into the input collection of bounding boxes representing the selected boxes. The bounding box coordinates corresponding to the selected indices can then be obtained using the tf.gather operation. For example: selected_indices = tf.image.non_max_suppression( boxes, scores, max_output_size, iou_threshold) selected_boxes = tf.gather(boxes, selected_indices)


X.get_shape().as_list()

tf.reduce_sum(tf.square(tf.subtract(a_C_unrolled, a_G_unrolled)))

GA = tf.matmul(A, tf.transpose(A))
