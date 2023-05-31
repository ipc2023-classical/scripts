;; +-+ +-+-+-+
;; |.|2|. 1 .|
;; + + +-+ +-+
;; |.|2 .|2|. 
;; + +-+-+ +-+
;; |2 . . . 3|
;; +-+-+-+-+-+

(define (problem sliterlink-3-5-966236)
(:domain slitherlink)

(:objects
    cap-0 cap-1 cap-2 cap-3 cap-4 - cell-capacity-level
    n-0-0 n-0-1 n-0-2 n-0-3 n-0-4 n-0-5 n-1-0 n-1-1 n-1-2 n-1-3 n-1-4 n-1-5 n-2-0 n-2-1 n-2-2 n-2-3 n-2-4 n-2-5 n-3-0 n-3-1 n-3-2 n-3-3 n-3-4 n-3-5 - node
    cell-0-0 cell-0-1 cell-0-2 cell-0-3 cell-0-4 cell-1-0 cell-1-1 cell-1-2 cell-1-3 cell-1-4 cell-2-0 cell-2-1 cell-2-2 cell-2-3 cell-2-4 cell-outside-0-left cell-outside-0-right cell-outside-1-left cell-outside-1-right cell-outside-2-left cell-outside-2-right cell-outside-0-up cell-outside-0-down cell-outside-1-up cell-outside-1-down cell-outside-2-up cell-outside-2-down cell-outside-3-up cell-outside-3-down cell-outside-4-up cell-outside-4-down - cell
)

(:init
    (cell-capacity-inc cap-0 cap-1)
    (cell-capacity-inc cap-1 cap-2)
    (cell-capacity-inc cap-2 cap-3)
    (cell-capacity-inc cap-3 cap-4)

    (cell-capacity cell-0-0 cap-4)
    (cell-capacity cell-0-1 cap-2)
    (cell-capacity cell-0-2 cap-4)
    (cell-capacity cell-0-3 cap-1)
    (cell-capacity cell-0-4 cap-4)
    (cell-capacity cell-1-0 cap-4)
    (cell-capacity cell-1-1 cap-2)
    (cell-capacity cell-1-2 cap-4)
    (cell-capacity cell-1-3 cap-2)
    (cell-capacity cell-1-4 cap-4)
    (cell-capacity cell-2-0 cap-2)
    (cell-capacity cell-2-1 cap-4)
    (cell-capacity cell-2-2 cap-4)
    (cell-capacity cell-2-3 cap-4)
    (cell-capacity cell-2-4 cap-3)
    (cell-capacity cell-outside-0-left cap-1)
    (cell-capacity cell-outside-0-right cap-1)
    (cell-capacity cell-outside-1-left cap-1)
    (cell-capacity cell-outside-1-right cap-1)
    (cell-capacity cell-outside-2-left cap-1)
    (cell-capacity cell-outside-2-right cap-1)
    (cell-capacity cell-outside-0-up cap-1)
    (cell-capacity cell-outside-0-down cap-1)
    (cell-capacity cell-outside-1-up cap-1)
    (cell-capacity cell-outside-1-down cap-1)
    (cell-capacity cell-outside-2-up cap-1)
    (cell-capacity cell-outside-2-down cap-1)
    (cell-capacity cell-outside-3-up cap-1)
    (cell-capacity cell-outside-3-down cap-1)
    (cell-capacity cell-outside-4-up cap-1)
    (cell-capacity cell-outside-4-down cap-1)

    (node-degree0 n-0-0)
    (node-degree0 n-0-1)
    (node-degree0 n-0-2)
    (node-degree0 n-0-3)
    (node-degree0 n-0-4)
    (node-degree0 n-0-5)
    (node-degree0 n-1-0)
    (node-degree0 n-1-1)
    (node-degree0 n-1-2)
    (node-degree0 n-1-3)
    (node-degree0 n-1-4)
    (node-degree0 n-1-5)
    (node-degree0 n-2-0)
    (node-degree0 n-2-1)
    (node-degree0 n-2-2)
    (node-degree0 n-2-3)
    (node-degree0 n-2-4)
    (node-degree0 n-2-5)
    (node-degree0 n-3-0)
    (node-degree0 n-3-1)
    (node-degree0 n-3-2)
    (node-degree0 n-3-3)
    (node-degree0 n-3-4)
    (node-degree0 n-3-5)

    (cell-edge cell-0-0 cell-1-0 n-1-0 n-1-1)
    (cell-edge cell-0-1 cell-1-1 n-1-1 n-1-2)
    (cell-edge cell-0-2 cell-1-2 n-1-2 n-1-3)
    (cell-edge cell-0-3 cell-1-3 n-1-3 n-1-4)
    (cell-edge cell-0-4 cell-1-4 n-1-4 n-1-5)
    (cell-edge cell-1-0 cell-2-0 n-2-0 n-2-1)
    (cell-edge cell-1-1 cell-2-1 n-2-1 n-2-2)
    (cell-edge cell-1-2 cell-2-2 n-2-2 n-2-3)
    (cell-edge cell-1-3 cell-2-3 n-2-3 n-2-4)
    (cell-edge cell-1-4 cell-2-4 n-2-4 n-2-5)
    (cell-edge cell-outside-0-up cell-0-0 n-0-0 n-0-1)
    (cell-edge cell-2-0 cell-outside-0-down n-3-0 n-3-1)
    (cell-edge cell-outside-1-up cell-0-1 n-0-1 n-0-2)
    (cell-edge cell-2-1 cell-outside-1-down n-3-1 n-3-2)
    (cell-edge cell-outside-2-up cell-0-2 n-0-2 n-0-3)
    (cell-edge cell-2-2 cell-outside-2-down n-3-2 n-3-3)
    (cell-edge cell-outside-3-up cell-0-3 n-0-3 n-0-4)
    (cell-edge cell-2-3 cell-outside-3-down n-3-3 n-3-4)
    (cell-edge cell-outside-4-up cell-0-4 n-0-4 n-0-5)
    (cell-edge cell-2-4 cell-outside-4-down n-3-4 n-3-5)
    (cell-edge cell-0-0 cell-0-1 n-0-1 n-1-1)
    (cell-edge cell-1-0 cell-1-1 n-1-1 n-2-1)
    (cell-edge cell-2-0 cell-2-1 n-2-1 n-3-1)
    (cell-edge cell-0-1 cell-0-2 n-0-2 n-1-2)
    (cell-edge cell-1-1 cell-1-2 n-1-2 n-2-2)
    (cell-edge cell-2-1 cell-2-2 n-2-2 n-3-2)
    (cell-edge cell-0-2 cell-0-3 n-0-3 n-1-3)
    (cell-edge cell-1-2 cell-1-3 n-1-3 n-2-3)
    (cell-edge cell-2-2 cell-2-3 n-2-3 n-3-3)
    (cell-edge cell-0-3 cell-0-4 n-0-4 n-1-4)
    (cell-edge cell-1-3 cell-1-4 n-1-4 n-2-4)
    (cell-edge cell-2-3 cell-2-4 n-2-4 n-3-4)
    (cell-edge cell-outside-0-left cell-0-0 n-0-0 n-1-0)
    (cell-edge cell-0-4 cell-outside-0-right n-0-5 n-1-5)
    (cell-edge cell-outside-1-left cell-1-0 n-1-0 n-2-0)
    (cell-edge cell-1-4 cell-outside-1-right n-1-5 n-2-5)
    (cell-edge cell-outside-2-left cell-2-0 n-2-0 n-3-0)
    (cell-edge cell-2-4 cell-outside-2-right n-2-5 n-3-5)
)
(:goal
    (and
        (not (node-degree1 n-0-0))
        (not (node-degree1 n-0-1))
        (not (node-degree1 n-0-2))
        (not (node-degree1 n-0-3))
        (not (node-degree1 n-0-4))
        (not (node-degree1 n-0-5))
        (not (node-degree1 n-1-0))
        (not (node-degree1 n-1-1))
        (not (node-degree1 n-1-2))
        (not (node-degree1 n-1-3))
        (not (node-degree1 n-1-4))
        (not (node-degree1 n-1-5))
        (not (node-degree1 n-2-0))
        (not (node-degree1 n-2-1))
        (not (node-degree1 n-2-2))
        (not (node-degree1 n-2-3))
        (not (node-degree1 n-2-4))
        (not (node-degree1 n-2-5))
        (not (node-degree1 n-3-0))
        (not (node-degree1 n-3-1))
        (not (node-degree1 n-3-2))
        (not (node-degree1 n-3-3))
        (not (node-degree1 n-3-4))
        (not (node-degree1 n-3-5))

        (cell-capacity cell-0-1 cap-0)
        (cell-capacity cell-0-3 cap-0)
        (cell-capacity cell-1-1 cap-0)
        (cell-capacity cell-1-3 cap-0)
        (cell-capacity cell-2-0 cap-0)
        (cell-capacity cell-2-4 cap-0)
    )
)
)


