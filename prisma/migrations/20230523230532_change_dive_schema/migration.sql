/*
  Warnings:

  - A unique constraint covering the columns `[name]` on the table `Dive` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "Dive_name_key" ON "Dive"("name");
