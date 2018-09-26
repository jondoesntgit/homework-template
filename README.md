# Jonathan Wheeler's LaTeX Homework Template

This is a template that I use to do my homework writeups at Stanford University. It was forked off of [this template](https://gist.github.com/seldonPlan/3420170)
Check out the compiled .pdf file. If you like it, and start using it, please leave a star on GitHub so that others can find this too!

## Installation

You will obviously need to have LaTeX installed on your
computer. Use tools like brew to do this.

From here, there will be several other packages that will need
to be installed, such as minted for code formatting, etc...

## Template

I've included a sample homework file with two sample problems.

For simplicity, it is easier to split things into individual files. You can either associate all the files for a particular problem in a folder together, or you can put types of files (images, code, etc...) in folders together.
This comes down to personal preference.

If you are working on a large homework assignment, and it takes time to build everything, you may consider using something like the sample Makefile.

If you clone this repository for a homework assignment, there will be a few things that you will have to do (primarily in sample.tex)

1. Update your name
2. Update the homework name
3. Update the list of collaborators (if any)
4. Create separate files for each problem.
5. (Optional) Update the Makefile

## Writing Problems

Problems can be started with the `\problem` directive. This creates a table of contents entry, and increments the problem number.

A problem can have subparts (which are alphabetically incremented) using the `enumerate` environment.

The solution can be shown using the `\solution` directive, which can be broken down into parts using `\part`.

## Contributing

Feel free to fork or contribute back to this repository. If you have any questions or concerns, list them in the Github Issue tracker.
