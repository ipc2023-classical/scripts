;; Generated with ./generator.py 2
(define
(problem rubiks-cube-shuffle-2)
(:domain rubiks-cube)
(:objects yellow white blue green orange red)
(:init
    (cube1 red white blue)
    (cube2 orange blue yellow)
    (cube3 green yellow red)
    (cube4 blue yellow red)
    (cube5 red white green)
    (cube6 orange blue white)
    (cube7 white green orange)
    (cube8 yellow green orange)
    (edge12 white blue)
    (edge24 orange yellow)
    (edge34 yellow red)
    (edge13 red blue)
    (edge15 red white)
    (edge26 orange blue)
    (edge48 blue yellow)
    (edge37 green yellow)
    (edge56 white green)
    (edge68 orange white)
    (edge78 green orange)
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

