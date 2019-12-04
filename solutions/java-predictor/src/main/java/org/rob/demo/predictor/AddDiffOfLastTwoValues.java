/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.rob.demo.predictor;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.PrintWriter;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Heiko Mueller <heiko.mueller@nyu.edu>
 */
public class AddDiffOfLastTwoValues {
    
    public static void main(String[] args) {
        
        if (args.length != 2) {
            System.out.println("Usage: <input-file> <output-file>");
            System.exit(-1);
        }
        
        File inputFile = new File(args[0]);
        File outputFile = new File(args[1]);

        File outputFolder = outputFile.getParentFile();
        if (outputFolder != null) {
            if (!outputFolder.exists()) {
                outputFolder.mkdirs();
            }
        }
        
        try (
                BufferedReader in = new BufferedReader(new FileReader(inputFile));
                PrintWriter out = new PrintWriter(new FileWriter(outputFile))
        ) {
            String line;
            while ((line = in.readLine()) != null) {
                if (!line.trim().equals("")) {
                    String[] tokens = line.split(":");
                    String seqId = tokens[0];
                    String[] values = tokens[1].split(",");
                    int last = Integer.parseInt(values[values.length - 1]);
                    int nextToLast = Integer.parseInt(values[values.length - 2]);
                    int prediction = last + (last - nextToLast);
                    out.println(seqId + ":" + prediction);
                }
            }
        } catch (java.io.IOException ex) {
            Logger.getGlobal().log(Level.SEVERE, "RUN", ex);
            System.exit(-1);
        }
    }
}
