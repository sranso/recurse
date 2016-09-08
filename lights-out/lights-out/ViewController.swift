//
//  ViewController.swift
//  lights-out
//
//  Created by Sarah Ransohoff on 9/7/16.
//  Copyright © 2016 Sarah Ransohoff. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet var cell0: UIButton!
    @IBOutlet var cell1: UIButton!
    @IBOutlet var cell2: UIButton!
    @IBOutlet var cell3: UIButton!
    @IBOutlet var cell4: UIButton!
    @IBOutlet var cell5: UIButton!
    @IBOutlet var cell6: UIButton!
    @IBOutlet var cell7: UIButton!
    @IBOutlet var cell8: UIButton!
    
    var cellArray: [ [UIButton] ] {
        get {
            return [ [cell0, cell1, cell2],
              [cell3, cell4, cell5],
              [cell6, cell7, cell8] ]
        }
    }

    let images: [UIImage] = [UIImage(named: "lights-on-square")!, UIImage(named: "lights-out-square")!]

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    func toggleCell(cell: UIButton) {
        if cell.backgroundImageForState(.Normal) == images[0] {
            cell.setBackgroundImage(images[1], forState: .Normal)
        } else {
            cell.setBackgroundImage(images[0], forState: .Normal)
        }
    }
    
    @IBAction func pressButton(sender: UIButton) {
        let tag = sender.tag
        let (x, y) = (tag / 3 , tag % 3)
        toggleCell(sender)
        if x > 0 {
            toggleCell(cellArray[x-1][y])
        }
        if y > 0 {
            toggleCell(cellArray[x][y-1])
        }
        if x < 2 {
            toggleCell(cellArray[x+1][y])
        }
        if y < 2 {
            toggleCell(cellArray[x][y+1])
        }
    }
    
    @IBAction func reset() {
        for row in cellArray {
            for cell in row {
                cell.setBackgroundImage(images[0], forState: .Normal)
            }
        }
    }


}

