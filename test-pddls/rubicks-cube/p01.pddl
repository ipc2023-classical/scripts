;; Generated with ./generator.py 1
(define
(problem rubicks-cube-shuffle-1)
(:domain rubicks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 red white blue)
    (cube2 orange green white)
    (cube3 red yellow blue)
    (cube4 orange blue white)
    (cube5 red white green)
    (cube6 orange green yellow)
    (cube7 red yellow green)
    (cube8 orange blue yellow)
    (edge12 white blue)
    (edge24 orange white)
    (edge34 yellow blue)
    (edge13 red blue)
    (edge15 red white)
    (edge26 orange green)
    (edge48 orange blue)
    (edge37 red yellow)
    (edge56 white green)
    (edge68 orange yellow)
    (edge78 yellow green)
    (edge57 red green)
)
(:goal
    (and
        (cube1 red white blue)
        (cube2 orange white blue)
        (cube3 red yellow blue)
        (cube4 orange yellow blue)
        (cube5 red white green)
        (cube6 orange white green)
        (cube7 red yellow green)
        (cube8 orange yellow green)

        (edge12 white blue)
        (edge24 orange blue)
        (edge34 yellow blue)
        (edge13 red blue)

        (edge15 red white)
        (edge26 orange white)
        (edge48 orange yellow)
        (edge37 red yellow)

        (edge56 white green)
        (edge68 orange green)
        (edge78 yellow green)
        (edge57 red green)

    )
)
)

